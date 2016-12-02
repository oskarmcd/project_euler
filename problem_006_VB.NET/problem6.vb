Module Module1

    Sub Main()
        Dim SumOfSquare As Integer = 0
        Dim SumOfNaturalNumbers As Integer = 0
        Dim SquareOfSum As Integer = 0
        For x = 1 To 100
            SumOfSquare = SumOfSquare + Squared(x)
        Next
        For x = 1 To 100
            SumOfNaturalNumbers = x + SumOfNaturalNumbers
        Next
        SquareOfSum = Squared(SumOfNaturalNumbers)
        Console.WriteLine(SquareOfSum - SumOfSquare)
        Console.ReadLine()
    End Sub
    Function Squared(ByVal Value As Integer)
        Squared = Value * Value
    End Function

End Module
