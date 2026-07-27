//! runkb — non-interactive batch runner: load a KB file, run pinned queries.
//! Usage: runkb <script>. Script lines: `:load <file>`, `? <query>`, `:contradictions`,
//! `#` comments, blank lines; anything else is asserted.

use nibli_engine::{NibliEngine, display_query_result};
use std::fs;

fn main() {
    let script = std::env::args().nth(1).expect("usage: runkb <script>");
    let engine = NibliEngine::new();
    let text = fs::read_to_string(&script).expect("read script");
    for (n, raw) in text.lines().enumerate() {
        let line = raw.trim();
        if line.is_empty() || line.starts_with('#') {
            continue;
        }
        if let Some(f) = line.strip_prefix(":load ") {
            let kb = fs::read_to_string(f.trim()).expect("read kb");
            let (mut ok, mut err) = (0u32, 0u32);
            for (kn, kraw) in kb.lines().enumerate() {
                let kl = kraw.trim();
                if kl.is_empty() || kl.starts_with('#') {
                    continue;
                }
                match engine.assert_text(kl) {
                    Ok(_) => ok += 1,
                    Err(e) => {
                        err += 1;
                        println!("[LoadErr] {}:{}: {} | {}", f.trim(), kn + 1, kl, e);
                    }
                }
            }
            println!("[Load] {} asserted={} errors={}", f.trim(), ok, err);
        } else if line == ":contradictions" {
            let v = engine.check_contradictions();
            println!("[Contradictions] {} found", v.len());
            for c in v {
                println!("  - {}", c);
            }
        } else if let Some(q) = line.strip_prefix('?') {
            match engine.query_text_with_proof(q.trim()) {
                Ok((r, _, _)) => println!("[Q] {} => {}", q.trim(), display_query_result(&r)),
                Err(e) => println!("[Q] {} => ERROR {}", q.trim(), e),
            }
        } else {
            match engine.assert_text(line) {
                Ok(_) => println!("[Assert] {}", line),
                Err(e) => println!("[AssertErr] line {}: {} | {}", n + 1, line, e),
            }
        }
    }
}
