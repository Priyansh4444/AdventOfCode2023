use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

fn calculate_hash<T: Hash>(t: T) -> u64 {
    let mut s = DefaultHasher::new();
    t.hash(&mut s);
    s.finish()
}

fn main() {
    println!("{}", calculate_hash(1.0f64));
    println!("{}", calculate_hash(1));
    println!("{}", calculate_hash(true));
}