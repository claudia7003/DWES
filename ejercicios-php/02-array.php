<?php

$elementos = [ ];
for ($i=0; $i < 10 ; $i++) { 
    $elementos[$i] =rand(1,30);
}
for ($i=0; $i < 10; $i++) { 
    echo "Posicion " .$i+1 . ": " . $elementos[$i] . "<br>";
}

?>