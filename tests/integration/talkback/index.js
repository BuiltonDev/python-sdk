const talkback = require("talkback");
const path = require('path');

function nameGenerator(tapeNumber, tape) {
    const urlParts = tape.req.url.split('/').filter(s => s);
    let handlerPart = "root";
    let remainder = "";
    if (urlParts.length > 0) {
        handlerPart = urlParts[0];
        remainder = urlParts.slice(1, urlParts.length).join("-")
    }
    return path.join(handlerPart, `${tape.req.method}-${remainder}-${tapeNumber}`);
}


const opts = {
    host: "https://qa.builton.dev",
    port: 5544,
    path: __dirname + "/tapes",
    name: "BuiltOn",
    debug: true,
    ignoreHeaders: ['authorization'],
    tapeNameGenerator: nameGenerator,
    record: talkback.Options.RecordMode.NEW // use DISABLED for test running
};
const server = talkback(opts);
server.start();
//server.close();

