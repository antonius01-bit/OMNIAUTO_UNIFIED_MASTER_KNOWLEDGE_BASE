On Error Resume Next
Set Voice = CreateObject("SAPI.SpVoice")
Voice.Volume = 100
Voice.Rate = 0

' Attempt to find a natural male voice if installed, otherwise default
For Each V In Voice.GetVoices
    If InStr(1, V.GetDescription, "David", 1) > 0 Or InStr(1, V.GetDescription, "George", 1) > 0 Then
        Set Voice.Voice = V
        Exit For
    End If
Next

If WScript.Arguments.Count > 0 Then
    Voice.Speak WScript.Arguments(0)
Else
    Voice.Speak "Welcome back, sir. Stark Industries neural grid online."
End If
