Module Module1

    Sub Main()
        Dim booleanvalue As Boolean
        Dim x As Integer = 1
        Do Until booleanvalue = True
            If x Mod 20 = 0 And x Mod 19 = 0 And x Mod 18 = 0 And x Mod 17 = 0 And x Mod 16 = 0 And x Mod 15 = 0 And x Mod 14 = 0 And x Mod 13 = 0 And x Mod 12 = 0 And x Mod 11 = 0 And x Mod 10 = 0 And x Mod 9 = 0 And x Mod 8 = 0 And x Mod 7 = 0 And x Mod 6 = 0 And x Mod 5 = 0 And x Mod 4 = 0 And x Mod 3 = 0 And x Mod 2 = 0 And x Mod 1 = 0 Then
                booleanvalue = True
            Else
                x = x + 1
            End If
        Loop
        Console.WriteLine(x)
        Console.ReadLine()
    End Sub

End Module
