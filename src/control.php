<?php

$cmd = htmlspecialchars($_GET["command"]);
error_log("arg is " . $cmd);
$command = escapeshellcmd('/usr/bin/python3 /usr/local/bin/robotcontrol.py ' . $cmd) . " 2>&1";
error_log("command is " . $command);
$output = shell_exec($command);
error_log("command out is " . $output);
echo $output;

?>
