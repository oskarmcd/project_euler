Module Module1

    Sub Main()
        Dim SumVals As Integer
        SumVals = 0
        For x = 0 To 999
            If (x / 3) = Int(x / 3) Or (x / 5) = Int(x / 5) Then
                SumVals = SumVals + x
            End If
        Next
        Console.WriteLine(SumVals)
        Console.ReadLine()
    End Sub

End Module
