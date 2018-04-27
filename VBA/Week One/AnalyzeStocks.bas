Attribute VB_Name = "Module2"
Sub AnalyzeStocks2()
'Variables: count: sequential dashboard placement
Dim count As Integer
Dim i As Long
Dim BeginningPrice As Double
Dim EndPrice As Double
Dim AnnualChange As Double
Dim PercentChange As Double
Dim TotalVolume As Double

' Loop Between worksheets
For Each ws In Worksheets

    'Determine the last row for the table and the subtable
    LastRow = ws.Cells(Rows.count, 1).End(xlUp).Row
    sublastrow = ws.Cells(Rows.count, 9).End(xlUp).Row
    
    'Print column titles for summarized tables
    ws.Cells(1, 9) = "Ticker"
    ws.Cells(1, 10) = "Yearly Change"
    ws.Cells(1, 11) = "Percent Change"
    ws.Cells(1, 12) = "Total Stock Volume"
    ws.Cells(1, 15) = "Ticker"
    ws.Cells(1, 16) = "Value"
    ws.Cells(2, 14) = "Greatest % Increase"
    ws.Cells(3, 14) = "Greatest % Decrease"
    ws.Cells(4, 14) = "Greatest Total Volume"
    
    'Count places the ticker/scores into the summarized table
    count = 2
    TotalVolume = 0
    
    'Conditional Formatting column J
    For j = 2 To sublastrow
        If ws.Cells(j, 10) > 0 Then
            ws.Cells(j, 10).Interior.ColorIndex = 4
        Else: ws.Cells(j, 10).Interior.ColorIndex = 3
        End If
    Next j
    
'Loop between Tickers and Grab the high, low of the year & total volume of trades
    For i = 2 To LastRow
        If ws.Cells(i, 1).Value <> ws.Cells(i - 1, 1).Value Then
            BeginningPrice = ws.Cells(i, 3).Value
        ElseIf ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
            TotalVolume = TotalVolume + ws.Cells(i, 7).Value
            EndPrice = ws.Cells(i, 6).Value
            ws.Cells(count, 9).Value = ws.Cells(i, 1).Value
            ws.Cells(count, 8).Value = BeginningPrice
            If BeginningPrice = 0 Then
                ws.Cells(count, 11) = "N/A"
                AnnualChange = EndPrice - BeginningPrice
            Else
                AnnualChange = EndPrice - BeginningPrice
                PercentChange = AnnualChange / BeginningPrice
                ws.Cells(count, 11).Value = PercentChange
            End If
            ws.Cells(count, 10).Value = AnnualChange
            ws.Cells(count, 12).Value = TotalVolume
            ws.Cells(count, 11).NumberFormat = "0.00%"
            
            'increment count & return cumulative values to zero
            count = count + 1
            TotalVolume = 0
        Else
            TotalVolume = TotalVolume + ws.Cells(i, 7).Value
        End If
    Next i
    
    
' edit loop to save values to "Greatest % Increase", "Greatest % Decrease" and "Greatest total volume".
Dim GreatInc
Dim GreatDec
Dim GreatVol
GreatInc = 0
GreatDec = 0
GreatVol = 0
    For k = 2 To sublastrow
        If ws.Cells(k, 11).Value > GreatInc Then
            ws.Cells(2, 15) = ws.Cells(k, 9)
            GreatInc = ws.Cells(k, 11).Value
            ws.Cells(2, 16) = GreatInc
        End If
        If ws.Cells(k, 11).Value < GreatDec Then
            ws.Cells(3, 15) = ws.Cells(k, 9)
            GreatDec = ws.Cells(k, 11).Value
            ws.Cells(3, 16) = GreatDec
        End If
        If ws.Cells(k, 12).Value > GreatVol Then
            ws.Cells(4, 15) = ws.Cells(k, 9)
            GreatVol = ws.Cells(k, 12)
            ws.Cells(4, 16) = GreatVol
        End If
    Next k
    ws.Range("P2:P3").NumberFormat = "0.00%"
    
Next ws
    
End Sub

