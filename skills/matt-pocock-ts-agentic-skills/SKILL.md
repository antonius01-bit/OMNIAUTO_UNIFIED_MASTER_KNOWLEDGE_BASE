---
name: matt-pocock-ts-agentic-skills
description: Elite TypeScript/JavaScript agentic engineering heuristics, modern API design, strict typing patterns, developer tooling automation, and Claude Code/Cursor integration skills.
---

# ⚡ Matt Pocock TypeScript Agentic Engineering Skills (S143)

## 📌 Overview & Core Architecture
The `matt-pocock-ts-agentic-skills` Super-Skill codifies Matt Pocock's world-renowned Total TypeScript heuristics, production design patterns, and agentic coding workflows:
1. **Type-Level Engineering & Zero-Cost Abstractions**: Conditional types, template literal types, mapped types, branded primitives, and inferred return type guarantees.
2. **Agentic Coding Prompt Tuning for TypeScript**: Explicit instructions that prevent AI models from generating loose types (`any`, `unknown` casts), unnecessary type assertions (`as Type`), or duplicated type definitions.
3. **Modern TypeScript Ecosystem Mastery**: Zod v3/v4 schema validation, TypeScript 5.x const type parameters, satisfies operator, decorators, and ESM package exports.
4. **Developer Tooling & CLI Automation**: Fast linting, automated refactor scripts, codemods, and vitest test-driven verification suites.

---

## ⚡ Core Operational Modes & Commands
- `/matt-pocock typecheck [file]`: Deeply audits a TypeScript module for loose types, unnecessary assertions, and unconstrained generics.
- `/ts-skills refactor [pattern]`: Applies modern TS 5.x patterns (`satisfies`, const type parameters, distributive conditional types).
- `/typescript-mastery zod-schema`: Generates bidirectional runtime-type-safe Zod schemas and inferred static TypeScript types.
- `/agent-ts generate`: Synthesizes fully typed, error-free MCP server tool handlers and client contracts.

---

## 💎 10 Commandments of Matt Pocock TypeScript Craftsmanship
1. **Never Use `as` Without Proof**: Type assertions silence the compiler and hide runtime bugs; use type narrowing and guards instead.
2. **Leverage `satisfies`**: Validate that an expression matches a type without widening its inferred specific shape.
3. **Brand Your Primitives**: Use `type UserId = string & { readonly __brand: unique symbol }` to prevent accidental ID cross-assignment.
4. **Prefer Generics Over Overloads**: Use conditional types and generic constraints rather than sprawling function signature overloads.
5. **Derive, Don't Duplicate**: Derive types from single sources of truth using `typeof`, `keyof`, `ReturnType`, and Zod schemas.
6. **Use Discriminated Unions**: Structure state with explicit `kind` or `status` discriminator tags for exhaustive pattern matching.
7. **Keep Types Local**: Co-locate types with implementation code; avoid massive global `types.d.ts` dumping grounds.
8. **Test Your Types**: Use `@ts-expect-error` and `expectTypeOf` (vitest) to write unit tests for your type definitions.
9. **Eliminate Non-Null Assertions (`!`)**: Always handle null/undefined explicitly or assert invariants with custom assertion functions.
10. **Zero Any Policy**: Treat `any` as a compile-time failure; use `unknown` with runtime narrowing for untyped external inputs.
