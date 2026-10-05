<?php
//Un array de temp, calcular media, max y min. Mostrar todos los valores calculados
//Array aleatorio y del 1,30

$temperatura = [];
for($i = 0; $i < 10; $i++){
    $temperatura[$i] = rand(1,30);
}
for ($i=0; $i < 10; $i++) { 
    echo "La temperatura es " .$i+1 . ": " . $temperatura[$i] . "<br>";
}
$suma = array_sum($temperatura);
$total_num = count($temperatura);
$media = $suma / $total_num;
echo "La media es: " .$media. "<br>";
echo "El valor maximo es:" .max($temperatura). "<br>";
echo "El valor minimo es:" .min($temperatura). "<br>";
?>