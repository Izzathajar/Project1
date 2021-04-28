<?php
    $decode = file_get_contents("data.json");
    //$myfile = fopen("data.json", "r") or die("Unable to open file!");
    //echo fread($myfile,filesize("webdictionary.txt"));
    //print_r(json_decode($decode));
    //echo($myfile->data);
    $decode = json_decode($decode);
    $array = $decode->data;
    $vul = $array[0];
    // echo("Low vulnerability: <br>");
    // print_r($decode1->{"Low-vulnerability"}[0]);
    // echo("<br><br> Medium-vulnerability: <br>");
    // print_r($decode1->{"Medium-vulnerability"});
    // echo("<br><br> High-vulnerability: <br>");
    // print_r($decode1->{"High-vulnerability"});
    // echo("<br><br> Cms-info: <br>");
    // print_r($decode1->{"Cms-info"});

    $test = $array[1];
    echo("Food: <br>");
    print_r($test->{"Shop"}[1]->{"Mcd"});

    //cara panggil object {}
    //$decode1->{"Cms-info"}

    //cara panggil array []
    //$decode1[0]

?>