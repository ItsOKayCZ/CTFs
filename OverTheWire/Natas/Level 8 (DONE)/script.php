<?php

$secret = "3d3d516343746d4d6d6c315669563362";

$secret = base64_decode(strrev(pack("H*", $secret)));

print $secret . "\n";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_decode($secret)));
}

?>