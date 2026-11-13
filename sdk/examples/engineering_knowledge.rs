//! Dependency-free Rust caller. The native CALF process owns all knowledge logic.
//! rustc --edition=2021 engineering_knowledge.rs -o knowledge-example
//! knowledge-example /absolute/path/to/calf /absolute/data/home [QUERY]
use std::{env, io::{self, Read, Write}, path::Path, process::{Command, Stdio}};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<_> = env::args().collect();
    if !(3..=4).contains(&args.len())
        || !Path::new(&args[1]).is_absolute() || !Path::new(&args[2]).is_absolute()
        || [args[1].as_str(), args[2].as_str()].iter().any(|p| Path::new(p).components().any(|c| c == std::path::Component::ParentDir)) {
        return Err("Provide the native executable and an explicit absolute data home".into());
    }
    let query = args.get(3).map(String::as_str).unwrap_or("database query performance");
    let mut child = Command::new(&args[1]).args(["knowledge", "resolve", query])
        .env("CALF_WORK_HOME", &args[2]).stdin(Stdio::null())
        .stdout(Stdio::piped()).stderr(Stdio::null()).spawn()?;
    let mut bytes=Vec::new();
    child.stdout.take().ok_or("Missing reference output")?.take(1024 * 1024 + 1).read_to_end(&mut bytes)?;
    if bytes.len() > 1024 * 1024 { let _=child.kill(); let _=child.wait(); return Err("Reference output exceeds limit".into()); }
    if !child.wait()?.success() {
        return Err("Reference query failed; no completion or execution authority is implied".into());
    }
    // Display reference JSON. A successful query is not a passing work check.
    io::stdout().write_all(&bytes)?;
    Ok(())
}
