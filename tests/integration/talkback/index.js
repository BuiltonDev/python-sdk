const talkback = require("talkback");

const opts = {
    host: "https://qa.kvass.ai",
    port: 5544,
    path: __dirname + "/tapes",
    name: "KvassAI",
    debug: true,
    ignoreHeaders: ['authorization'],
};
const server = talkback(opts);
server.start();
//server.close();

