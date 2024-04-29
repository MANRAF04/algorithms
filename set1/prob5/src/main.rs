pub fn tallest(array: Vec<Vec<i8>>) -> i32 {
    let mut top = 0;
    let mut bot = array.len();
    let mut col = -1;
    let mut k;

    while top != bot {
        let mid = (top + bot) / 2;
        let mut curr = -1;
        k = 0;
        for i in &array[mid] {
            if *i == 0 {
                col = k;
                curr = k;
                break;
            }
            k += 1;
        }

        if curr == -1 {
            top = mid + 1;
        } else {
            bot = mid;
        }
    } 
    col
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn no_building() {
        let array = vec![vec![1, 1, 1, 1, 1]];

        assert_eq!(tallest(array), -1)
    }

    #[test]
    fn all_tallest() {
        let array = vec![
            vec![1, 1, 1, 1, 1],
            vec![0, 0, 0, 0, 0],
            vec![0, 0, 0, 0, 0],
            vec![0, 0, 0, 0, 0],
            vec![0, 0, 0, 0, 0],
            vec![0, 0, 0, 0, 0],
        ];

        assert_eq!(tallest(array), 0)
    }

    #[test]
    fn two_rows() {
        let array = vec![vec![1, 1, 1, 1, 1], vec![1, 1, 1, 0, 1]];

        assert_eq!(tallest(array), 3)
    }

    #[test]
    fn change_at_end_tallest() {
        let array = vec![
            vec![1, 1, 1, 1, 0],
            vec![0, 0, 0, 0, 0],
            vec![0, 0, 0, 0, 0],
            vec![0, 0, 0, 0, 0],
            vec![0, 0, 0, 0, 0],
            vec![0, 0, 0, 0, 0],
        ];

        assert_eq!(tallest(array), 4)
    }
}

fn main() {
    let array = vec![
        vec![1, 1, 1, 1, 1],
        vec![1, 1, 1, 1, 1],
        vec![1, 1, 1, 1, 1],
        vec![1, 1, 1, 1, 0],
        vec![1, 1, 1, 1, 0],
        vec![0, 1, 1, 1, 0],
        vec![0, 1, 0, 1, 0],
        vec![0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0],
    ];

    let building = tallest(array);
    if building >= 0 {
        println!("Building {} is the tallest in Farsala!", building);
    } else {
        println!("Farsala has no buildings :(");
    }
}
