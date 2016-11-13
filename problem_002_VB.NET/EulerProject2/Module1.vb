Module Module1

    Sub Main()
        Dim number As Int64 = "0802229738150039007504050778521250779108"
        Dim array(39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39) As Integer
        Dim x As Integer = 0
        Do Until x = 20
            array(x) = number.ToString()
        Loop
    End Sub
End Module
