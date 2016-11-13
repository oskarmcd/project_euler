Module Module1

    Sub Main()
        Dim value As Int32
        Dim highestvalue As Int32 = 0
        For x = 0 To 1000
            For y = 0 To 1000
                value = x * y
                If IsPalindrome(value) = True And value > highestvalue Then
                    highestvalue = value
                End If
            Next
        Next
        Console.WriteLine(highestvalue)
        Console.ReadLine()
    End Sub
    Function IsPalindrome(ByVal value As String)
        Dim length As Integer
        IsPalindrome = True
        length = (value.Length - 1)
        For x = 0 To length
            If value(x) <> value(length - x) Then
                IsPalindrome = False
            End If
        Next

    End Function

End Module
