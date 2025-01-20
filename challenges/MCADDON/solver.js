// .mcaddon : https://learn.microsoft.com/en-us/minecraft/creator/documents/minecraftfileextensions?view=minecraft-bedrock-stable
// DIJELASKAN BAHWA .mcaddon ADALAH 'zip file that contains .mcpack or .mcworld files to modify Minecraft (Bedrock Edition)'. LALU UNZIP
// STRUKTUR FOLDER HASIL UNZIP DAPAT DIPELAJARI DISINI : https://wiki.bedrock.dev/documentation/pack-structure

// TERLIHAT BAHWA TERDAPAT FILE main.js PADA FOLDER 'MC_FlagChecker BP/scripts/main.js' YANG MERUPAKAN SCRIPTS YANG DIMUAT DIDALAM FILE manifest.json

// "modules": [
//     {
//         "type": "data",
//         "uuid": "ade988a2-2744-40fe-8976-60fd84b0aaf9",
//         "version": [
//             1,
//             0,
//             0
//         ]
//     },
//     {
//         "type": "script",
//         "language": "javascript",
//         "uuid": "1dd1734d-26d8-4fd4-9f46-124775ad221a",
//         "entry": "scripts/main.js",
//         "version": [
//             1,
//             0,
//             0
//         ]
//     }
// ]

// DEOBFUSCATE KODE JS :

// import { world, system } from '@minecraft/server';
// world.afterEvents.playerSpawn.subscribe(_0x2c772d => {
//     system.runTimeout(() => {
//         const _0x438077 = _0x2c772d.player;
//         _0x438077.sendMessage("§eSend me the correct password through the chat and i'll give you the flag");
//     }, 100);
// });

// function enc(_0x400fff, _0x1b8ac5) {
//     var _0x30f4b4 = [];
//     var _0x507d16 = 0x0;
//     var _0x5b5a97;
//     var _0x3bbc73 = [];
//     for (var _0x1acd1e = 0x0; _0x1acd1e < 0x100; _0x1acd1e++) {
//         _0x30f4b4[_0x1acd1e] = _0x1acd1e;
//     }
//     for (_0x1acd1e = 0x0; _0x1acd1e < 0x100; _0x1acd1e++) {
//         _0x507d16 = (_0x507d16 + _0x30f4b4[_0x1acd1e] + _0x400fff.charCodeAt(_0x1acd1e % _0x400fff.length)) % 0x100;
//         _0x5b5a97 = _0x30f4b4[_0x1acd1e];
//         _0x30f4b4[_0x1acd1e] = _0x30f4b4[_0x507d16];
//         _0x30f4b4[_0x507d16] = _0x5b5a97;
//     }
//     _0x1acd1e = 0x0;
//     _0x507d16 = 0x0;
//     for (var _0x1129ba = 0x0; _0x1129ba < _0x1b8ac5.length; _0x1129ba++) {
//         _0x1acd1e = (_0x1acd1e + 0x1) % 0x100;
//         _0x507d16 = (_0x507d16 + _0x30f4b4[_0x1acd1e]) % 0x100;
//         _0x5b5a97 = _0x30f4b4[_0x1acd1e];
//         _0x30f4b4[_0x1acd1e] = _0x30f4b4[_0x507d16];
//         _0x30f4b4[_0x507d16] = _0x5b5a97;
//         _0x3bbc73.push(_0x1b8ac5.charCodeAt(_0x1129ba) ^ _0x30f4b4[(_0x30f4b4[_0x1acd1e] + _0x30f4b4[_0x507d16]) % 0x100]);
//     }
//     return _0x3bbc73;
// }

// world.afterEvents.chatSend.subscribe(_0x2360ea => {
//     const _0x175c97 = _0x2360ea.sender;
//     if (_0x175c97.level < 0x539) {
//         _0x175c97.resetLevel();
//         _0x175c97.sendMessage("§4Your level is too low :(");
//     } else {
//         if (_0x175c97.level > 0x539) {
//             _0x175c97.resetLevel();
//             _0x175c97.sendMessage("§4Your level is too high :(");
//         } else {
//             var _0x1afce5 = [0x26, 0x56, 0x89, 0x6c, 0xc0, 0x1, 0x2f, 0xd8, 0x72, 0x87, 0x79, 0xb6, 0x61, 0x97, 0xb6, 0x11];
//             if (_0x1afce5.length == _0x2360ea.message.length) {
//                 var _0x41564d = _0x175c97.level.toString();
//                 var _0x28a97a = enc(_0x41564d, _0x2360ea.message);
//                 for (var _0x32b2aa = 0x0; _0x32b2aa < _0x28a97a.length; _0x32b2aa++) {
//                     if (_0x1afce5[_0x32b2aa] !== _0x28a97a[_0x32b2aa]) {
//                         _0x175c97.resetLevel();
//                         _0x175c97.sendMessage("§4NO NO NO NO NO!!!!");
//                         break;
//                     }
//                 }
//                 if (_0x175c97.level == 0x539) {
//                     _0x175c97.sendMessage("§aYour flag is QUADRATHLON{" + _0x175c97.level + _0x2360ea.message + _0x175c97.level + '}');
//                 }
//             } else {
//                 _0x175c97.resetLevel();
//                 _0x175c97.sendMessage("§4NO NO NO NO NO!!!!");
//             }
//         }
//     }
// });

// FUNGSI enc() MERUPAKAN ENCRYPTION RC4. PROSES ENCRYPTION SAMA DENGAN DECRYPTION PADA RC4
// SEHINGGA GUNAKAN FUNGSI enc() YANG SUDAH TERSEDIA UNTUK MELAKUKAN DECRYPTION PADA ENCRYPTED FLAG

function enc(_0x400fff, _0x1b8ac5) {
    var _0x30f4b4 = [];
    var _0x507d16 = 0x0;
    var _0x5b5a97;
    var _0x3bbc73 = [];
    for (var _0x1acd1e = 0x0; _0x1acd1e < 0x100; _0x1acd1e++) {
        _0x30f4b4[_0x1acd1e] = _0x1acd1e;
    }
    for (_0x1acd1e = 0x0; _0x1acd1e < 0x100; _0x1acd1e++) {
        _0x507d16 = (_0x507d16 + _0x30f4b4[_0x1acd1e] + _0x400fff.charCodeAt(_0x1acd1e % _0x400fff.length)) % 0x100;
        _0x5b5a97 = _0x30f4b4[_0x1acd1e];
        _0x30f4b4[_0x1acd1e] = _0x30f4b4[_0x507d16];
        _0x30f4b4[_0x507d16] = _0x5b5a97;
    }
    _0x1acd1e = 0x0;
    _0x507d16 = 0x0;
    for (var _0x1129ba = 0x0; _0x1129ba < _0x1b8ac5.length; _0x1129ba++) {
        _0x1acd1e = (_0x1acd1e + 0x1) % 0x100;
        _0x507d16 = (_0x507d16 + _0x30f4b4[_0x1acd1e]) % 0x100;
        _0x5b5a97 = _0x30f4b4[_0x1acd1e];
        _0x30f4b4[_0x1acd1e] = _0x30f4b4[_0x507d16];
        _0x30f4b4[_0x507d16] = _0x5b5a97;
        _0x3bbc73.push(_0x1b8ac5.charCodeAt(_0x1129ba) ^ _0x30f4b4[(_0x30f4b4[_0x1acd1e] + _0x30f4b4[_0x507d16]) % 0x100]);
    }
    return _0x3bbc73;
}

var enc_flag = [
    38, 86, 137, 108, 192,
    1, 47, 216, 114, 135,
    121, 182, 97, 151, 182,
    17
];

var playerLVL = "1337";
enc_flag = enc_flag.map((x) => String.fromCharCode(x)).join("");
var m = enc(playerLVL, enc_flag);
var flag = playerLVL + m.map((x) => String.fromCharCode(x)).join("") + playerLVL;
console.log("QUADRATHLON{" + flag + "}");