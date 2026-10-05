<?php
//Rellenar array y calcular su valor medio

$numero = [];
for($i = 0; $i < 10; $i++){
    $numero[$i] = rand(1,30);
}
for ($i=0; $i < 10; $i++) { 
    echo "Posicion " .$i+1 . ": " . $numero[$i] . "<br>";
    
}
$suma = array_sum($numero);
$total_num = count($numero);
$media = $suma / $total_num;
echo "El calculo es: " .$media. "<br>";

?>