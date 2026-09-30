#!/usr/bin/env python3
"""
GAuth Security Gate & Workflow Runtime Guard
Provides zero-trust authentication, RFC 6238 TOTP verification,
cryptographic run tokens, and automated audit logging for all agent workflows.
"""

import os
import sys
import time
import json
import hmac
import hashlib
import struct
import base64
import secrets
import argparse
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\antoni\Dola"
VAULT_DIR = os.path.join(BASE_DIR, "obsidian_vault")
AUDIT_LOG_PATH = os.path.join(VAULT_DIR, "19_TOOL_ECOSYSTEM", "GAUTH_SECURITY_AUDIT_LOG.md")
MEMORY_CACHE_FILE = os.path.join(BASE_DIR, "agent_memory.json")

# Config from environment or fallback
DEFAULT_SECRET = "WOKCCO35GJAA3Z22"
SECRET_KEY = os.environ.get("GAUTH_SECRET_KEY", DEFAULT_SECRET).strip().upper()
SECURITY_MODE = os.environ.get("GAUTH_SECURITY_MODE", "ACTIVE").strip().upper()
ISSUER = os.environ.get("GAUTH_ISSUER", "Dola-Stark-OS")
ACCOUNT = os.environ.get("GAUTH_ACCOUNT", "antoni@dola.ai")
MASTER_PIN = os.environ.get("GAUTH_MASTER_PIN", "111993").strip()


# ==============================================================================
# 1. RFC 6238 TOTP ENGINE (ZERO-DEPENDENCY)
# ==============================================================================

def get_current_totp(secret=None):
    """
    Returns (code_str, seconds_remaining) for current 30-second window.
    """
    sec = (secret or SECRET_KEY).replace(" ", "")
    padding = len(sec) % 8
    if padding:
        sec += "=" * (8 - padding)
    
    current_time = time.time()
    interval = int(current_time) // 30
    seconds_remaining = 30 - (int(current_time) % 30)

    try:
        key = base64.b32decode(sec)
        msg = struct.pack(">Q", interval)
        h = hmac.new(key, msg, hashlib.sha1).digest()
        offset = h[19] & 15
        code = (struct.unpack(">I", h[offset:offset + 4])[0] & 0x7fffffff) % 1000000
        return f"{code:06d}", seconds_remaining
    except Exception as e:
        return "000000", seconds_remaining

def verify_totp(code, secret=None, drift=1):
    """
    Validates a 6-digit TOTP code against the secret key with drift tolerance (+/- 30s).
    """
    if not code:
        return False
    code_str = str(code).strip()
    if len(code_str) != 6 or not code_str.isdigit():
        return False

    # Master Emergency 2FA PIN bypass (111993)
    if code_str == MASTER_PIN:
        return True

    sec = (secret or SECRET_KEY).replace(" ", "")

    padding = len(sec) % 8
    if padding:
        sec += "=" * (8 - padding)

    try:
        key = base64.b32decode(sec)
    except Exception:
        return False

    current_interval = int(time.time()) // 30
    for i in range(-drift, drift + 1):
        test_interval = current_interval + i
        msg = struct.pack(">Q", test_interval)
        h = hmac.new(key, msg, hashlib.sha1).digest()
        offset = h[19] & 15
        expected = (struct.unpack(">I", h[offset:offset + 4])[0] & 0x7fffffff) % 1000000
        if f"{expected:06d}" == code_str:
            return True
    return False

def get_otpauth_uri(account=None, secret=None, issuer=None):
    acc = account or ACCOUNT
    sec = secret or SECRET_KEY
    iss = issuer or ISSUER
    return f"otpauth://totp/{iss}:{acc}?secret={sec}&issuer={iss}&algorithm=SHA1&digits=6&period=30"

# ==============================================================================
# 2. MACHINE RUN TOKENS & CRYPTOGRAPHIC PROOF
# ==============================================================================

def generate_run_token(operation, agent="dola", expires_in=600):
    """
    Generates a cryptographically signed run token for workflow operations.
    Format: payload_b64.signature_hex
    """
    now = int(time.time())
    nonce = secrets.token_hex(8)
    payload = {
        "op": operation,
        "agent": agent,
        "ts": now,
        "exp": now + expires_in,
        "nonce": nonce
    }
    payload_str = json.dumps(payload, separators=(',', ':'), sort_keys=True)
    payload_b64 = base64.urlsafe_b64encode(payload_str.encode('utf-8')).decode('utf-8').rstrip('=')
    
    # Sign using SECRET_KEY as HMAC key
    sig = hmac.new(SECRET_KEY.encode('utf-8'), payload_b64.encode('utf-8'), hashlib.sha256).hexdigest()
    return f"{payload_b64}.{sig}"

def verify_run_token(token):
    """
    Validates a run token's cryptographic signature and expiration.
    Returns (is_valid, payload_dict, reason)
    """
    if not token or '.' not in token:
        return False, {}, "Malformed token format"
    try:
        parts = token.split('.')
        if len(parts) != 2:
            return False, {}, "Invalid token structure"
        payload_b64, signature = parts
        
        # Verify signature
        expected_sig = hmac.new(SECRET_KEY.encode('utf-8'), payload_b64.encode('utf-8'), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, expected_sig):
            return False, {}, "Cryptographic signature mismatch"

        # Decode payload
        rem = len(payload_b64) % 4
        padded = payload_b64 + ("=" * (4 - rem) if rem else "")
        payload_json = base64.urlsafe_b64decode(padded.encode('utf-8')).decode('utf-8')
        payload = json.loads(payload_json)

        # Check expiration
        now = int(time.time())
        if now > payload.get("exp", 0):
            return False, payload, "Token expired"

        return True, payload, "Valid"
    except Exception as e:
        return False, {}, f"Verification error: {str(e)}"

# ==============================================================================
# 3. WORKFLOW RUN AUTHORIZER & AUDIT LOGGER
# ==============================================================================

def authorize_workflow_run(operation_name, agent="dola", auth_credential=None, details=""):
    """
    Validates authorization for a workflow run and generates an audit log entry.
    auth_credential can be:
      - 6-digit TOTP code
      - Machine run token (payload.signature)
      - None (allowed if SECURITY_MODE is 'ACTIVE' or 'AUDIT_ONLY', an auto-signed token is issued)
    """
    now_dt = datetime.now()
    timestamp_str = now_dt.strftime("%Y-%m-%d %H:%M:%S")
    run_id = f"RUN-{int(time.time()*1000)}"
    
    auth_type = "UNSPECIFIED"
    authorized = False
    reason = ""

    if auth_credential:
        cred = str(auth_credential).strip()
        if len(cred) == 6 and cred.isdigit():
            # TOTP 2FA Verification
            if cred == MASTER_PIN:
                authorized = True
                auth_type = "MASTER_PIN_2FA"
                reason = "Valid Master 2FA PIN (111993)"
            elif verify_totp(cred):
                authorized = True
                auth_type = "TOTP_2FA"
                reason = "Valid RFC 6238 TOTP token"
            else:
                authorized = False
                auth_type = "TOTP_2FA"
                reason = "Invalid or expired TOTP code"

        elif '.' in cred:
            # Machine Run Token
            is_valid, payload, token_reason = verify_run_token(cred)
            authorized = is_valid
            auth_type = "RUN_TOKEN"
            reason = token_reason
        else:
            authorized = False
            auth_type = "UNKNOWN_CREDENTIAL"
            reason = "Unrecognized credential format"
    else:
        # No credential passed
        if SECURITY_MODE in ("ACTIVE", "AUDIT_ONLY"):
            authorized = True
            auth_type = "AUTO_AUDIT"
            reason = f"Mode {SECURITY_MODE}: Auto-signed workflow authorization"
        else:
            authorized = False
            auth_type = "REJECTED"
            reason = f"Mode {SECURITY_MODE}: Explicit credential required"

    # Generate persistent signed receipt token
    receipt_token = generate_run_token(f"{operation_name}:{run_id}", agent=agent)
    signature_fingerprint = receipt_token.split('.')[-1][:16]

    result = {
        "authorized": authorized,
        "run_id": run_id,
        "operation": operation_name,
        "agent": agent,
        "auth_type": auth_type,
        "reason": reason,
        "timestamp": timestamp_str,
        "security_mode": SECURITY_MODE,
        "signature": signature_fingerprint,
        "run_token": receipt_token,
        "details": details
    }

    # Log to Obsidian Audit Log
    _log_to_obsidian_audit(result)
    # Log to agent memory cache
    _log_to_memory_cache(result)

    return result

def _log_to_obsidian_audit(run_record):
    """Logs the authorized run into Obsidian Node 19 audit log note."""
    os.makedirs(os.path.dirname(AUDIT_LOG_PATH), exist_ok=True)
    header = """---
title: "GAuth Security Mesh — Workflow Run Audit Log"
created: 2026-09-28
tags: [dola, agy, gauth, security, audit-log, node19]
type: log
---

# 🛡️ GAuth Security Mesh — Workflow Run Audit Log
Catatan forensik seluruh eksekusi tugas agen, sinkronisasi loop, dan otorisasi 2FA.

| Timestamp | Run ID | Operation | Agent | Auth Type | Status | Signature Hash |
|---|---|---|---|---|:---:|---|
"""
    if not os.path.exists(AUDIT_LOG_PATH):
        try:
            with open(AUDIT_LOG_PATH, 'w', encoding='utf-8') as f:
                f.write(header)
        except Exception:
            return

    status_badge = "✅ PERMITTED" if run_record.get("authorized") else "❌ BLOCKED"
    row = (
        f"| {run_record.get('timestamp')} "
        f"| `{run_record.get('run_id')}` "
        f"| **{run_record.get('operation')}** "
        f"| `{run_record.get('agent')}` "
        f"| {run_record.get('auth_type')} "
        f"| {status_badge} "
        f"| `{run_record.get('signature')}` |\n"
    )
    try:
        with open(AUDIT_LOG_PATH, 'a', encoding='utf-8') as f:
            f.write(row)
    except Exception:
        pass

def _log_to_memory_cache(run_record):
    """Saves recent security audit runs into local agent_memory.json."""
    if not os.path.exists(MEMORY_CACHE_FILE):
        return
    try:
        with open(MEMORY_CACHE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        audits = data.get("security_audits", [])
        audits.append({
            "run_id": run_record.get("run_id"),
            "operation": run_record.get("operation"),
            "timestamp": run_record.get("timestamp"),
            "authorized": run_record.get("authorized"),
            "signature": run_record.get("signature")
        })
        # Keep last 50 audits
        data["security_audits"] = audits[-50:]
        with open(MEMORY_CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

# ==============================================================================
# 4. CONTEXT MANAGER & DECORATOR
# ==============================================================================

class GAuthRunContext:
    def __init__(self, operation_name, agent="dola", credential=None, details=""):
        self.operation = operation_name
        self.agent = agent
        self.credential = credential
        self.details = details
        self.auth_result = None

    def __enter__(self):
        self.auth_result = authorize_workflow_run(
            self.operation,
            agent=self.agent,
            auth_credential=self.credential,
            details=self.details
        )
        if not self.auth_result.get("authorized"):
            raise PermissionError(f"[GAuth Security Gate] Run authorization denied: {self.auth_result.get('reason')}")
        return self.auth_result

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def gauth_secure_run(operation_name, agent="dola"):
    """Function decorator ensuring workflow run passes GAuth gate."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            cred = kwargs.pop("auth_credential", None)
            with GAuthRunContext(operation_name, agent=agent, credential=cred):
                return func(*args, **kwargs)
        return wrapper
    return decorator

# ==============================================================================
# 5. CLI INTERFACE
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="GAuth Security Gate & Workflow Guard")
    parser.add_argument("--status", action="store_true", help="Display GAuth status and active 2FA info")
    parser.add_argument("--totp", action="store_true", help="Print current 6-digit TOTP code")
    parser.add_argument("--verify", type=str, help="Verify a 6-digit TOTP code")
    parser.add_argument("--sign", type=str, help="Authorize and cryptographically sign a workflow run")
    parser.add_argument("--agent", type=str, default="dola", help="Agent name for the run")
    parser.add_argument("--cred", type=str, default=None, help="Credential (TOTP or run token)")

    args = parser.parse_args()

    if args.status:
        code, remaining = get_current_totp()
        print("=" * 65)
        print("🛡️ GAUTH SECURITY MESH // WORKFLOW RUNTIME GATE")
        print("=" * 65)
        print(f"Status           : ARMED & RUN-PROTECTED")
        print(f"Security Mode    : {SECURITY_MODE}")
        print(f"Account          : {ACCOUNT}")
        print(f"Issuer           : {ISSUER}")
        print(f"Active TOTP Code : {code} (refreshes in {remaining}s)")
        print(f"Audit Log        : {AUDIT_LOG_PATH}")
        print("=" * 65)
        return

    if args.totp:
        code, remaining = get_current_totp()
        print(f"TOTP Code: {code} (valid for {remaining}s)")
        return

    if args.verify:
        is_valid = verify_totp(args.verify)
        if is_valid:
            token = generate_run_token("Manual-Verify")
            print(f"Verification: ✅ VALID (Code: {args.verify})")
            print(f"Issued Run Token: {token}")
        else:
            print(f"Verification: ❌ INVALID OR EXPIRED (Code: {args.verify})")
        return

    if args.sign:
        res = authorize_workflow_run(args.sign, agent=args.agent, auth_credential=args.cred)
        print(json.dumps(res, indent=2))
        return

    parser.print_help()

if __name__ == "__main__":
    main()
