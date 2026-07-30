// Node <22 line: CommonJS, and no `node:`-prefixed builtin imports, so it loads
// on runtimes that predate them. The real constraint lives in package.json
// "engines" -- zed's manifest has no equivalent field.
const path = require("path");

module.exports.greet = (who) =>
  `hello ${who} from multiversion-lib/node18`;
module.exports.LANGUAGE = "nodejs";
module.exports.RUNTIME_LINE = "node18";
module.exports.SEP = path.sep;
