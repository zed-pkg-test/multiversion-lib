// Node >=22 line: native ESM plus `node:`-prefixed builtins. Loading this on
// the <22 line fails, which is the whole reason the two cannot share one
// artifact -- and why a consumer must be able to ask for one line specifically.
import { sep } from "node:path";

export const greet = (who) => `hello ${who} from multiversion-lib/node22`;
export const LANGUAGE = "nodejs";
export const RUNTIME_LINE = "node22";
export const SEP = sep;
