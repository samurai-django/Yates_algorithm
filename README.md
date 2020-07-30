# Yates_algorithm




<h2>Yate's sample.csv</h2>
<img src="https://latex.codecogs.com/gif.latex?2^{3}">要因実験

アルゴリズムは以下に示す。


<table>
<tr>
<th>Data</th><th>Step1</th><th>Step2</th><th>Step4</th>
</tr>
<tr>
<td><img src="https://latex.codecogs.com/gif.latex?y_{(1)}"></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{(1)}&space;&plus;&space;y_{a}"></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{(1)}&space;&plus;&space;y_{a}&space;&plus;&space;y_{b}&space;&plus;&space;y_{ab}"> </td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{(1)}&space;&plus;&space;y_{a}&space;&plus;&space;y_{b}&space;&plus;&space;y_{ab}&space;&plus;&space;y_{c}&space;&plus;&space;y_{ac}&space;&plus;&space;y_{bc}&space;&plus;&space;y_{abc}"></td>
</tr>
<tr>
<td><img src="https://latex.codecogs.com/gif.latex?y_{a}"></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{a}&space;&plus;&space;y_{ab}"></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{c}&space;&plus;&space;y_{ac}&space;&plus;&space;y_{bc}&space;&plus;&space;y_{abc}"></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{a}&space;-&space;y_{(1)}&space;&plus;&space;y_{ab}&space;-&space;y_{b}&space;&plus;&space;y_{ac}&space;-&space;y_{c}&space;&plus;&space;y_{abc}&space;-&space;y_{bc}"></td>
</tr>
<tr>
<td><img src="https://latex.codecogs.com/gif.latex?y_{b}"></td>
<td><img src=""></td>
<td><img src=""></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{b}&space;&plus;&space;y_{ab}&space;-&space;y_{(1)}&space;-&space;y_{a}&space;&plus;&space;y_{bc}&space;&plus;&space;y_{abc}&space;-&space;y_{c}&space;-&space;y_{ac}"></td>
</tr>
<tr>
<td><img src="https://latex.codecogs.com/gif.latex?y_{ab}"></td>
<td><img src=""></td>
<td><img src=""></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{ab}&space;-&space;y_{b}&space;-&space;y_{a}&space;&plus;&space;y_{(1)}&space;&plus;&space;y_{abc}&space;-&space;y_{bc}&space;-&space;y_{ac}&space;&plus;&space;y_{c}"></td>
</tr>
<tr>
<td><img src="https://latex.codecogs.com/gif.latex?y_{c}"></td>
<td><img src=""></td>
<td><img src=""></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{c}&space;&plus;&space;y_{ac}&space;&plus;&space;y_{bc}&space;&plus;&space;y_{abc}&space;-&space;y_{(1)}&space;-&space;y_{a}&space;-&space;y_{}&space;&plus;&space;y_{ab}"></td>
</tr>
<tr>
<td><img src="https://latex.codecogs.com/gif.latex?y_{ac}"></td>
<td><img src=""></td>
<td><img src=""></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{ac}&space;-&space;y_{c}&space;&plus;&space;y_{abc}&space;-&space;y_{bc}&space;-&space;y_{a}&space;&plus;&space;y_{(1)}&space;-&space;y_{ab}&space;&plus;&space;y_{b}"></td>
</tr>
<tr>
<td><img src="https://latex.codecogs.com/gif.latex?y_{bc}"></td>
<td><img src=""></td>
<td><img src=""></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{bc}&space;&plus;&space;y_{abc}&space;-&space;y_{c}&space;-&space;y_{ac}&space;-&space;y_{b}&space;-&space;y_{ab}&space;&plus;&space;y_{(1)}&space;&plus;&space;y_{a}"></td>
</tr>
<tr>
<td><img src="https://latex.codecogs.com/gif.latex?y_{abc}"></td>
<td><img src=""></td>
<td><img src=""></td>
<td><img src="https://latex.codecogs.com/gif.latex?y_{abc}&space;-&space;y_{bc}&space;-&space;y_{ac}&space;&plus;&space;y_{c}&space;-&space;y_{ab}&space;&plus;&space;y_{b}&space;&plus;&space;y_{a}&space;-&space;y_{(1)}"></td>
</tr>
</table>
