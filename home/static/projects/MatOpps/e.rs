
use std::collections::*;
use std::rc::Rc;
use std::cell::RefCell;
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}


pub fn is_complete_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>>{
    let complete: bool=true;
    /*let mut left_node=root;
    let mut right_node=None;

    while complete{
        if left_node.unwrap().left==None && right_node.unwrap().right!=None{
            complete=false;
        }else{
            left_node=left_node.left;
            right_node=left_node.right;
        }
    }*/

    root
}

fn complete_node(_next: Vec<Option<Rc<RefCell<TreeNode>>>>, level: i32) -> i32{
    let mut next=_next;
    let mut recur_next: Vec<Option<Rc<RefCell<TreeNode>>>>;
    for node in next.iter(){
        recur_next.push(node.as_ref().unwrap().borrow_mut().left.clone());
        recur_next.push(node.as_ref().unwrap().borrow_mut().right.clone());
    }
    
    if recur_next.iter().all(|item| item.as_ref().unwrap().borrow_mut().left  == first.unwrap().borrow_mut().left)
    {
        return 1;
    }
    complete_node(recur_next.clone(), recur_next.len() as i32)
}

fn main() {
    let node: Option<Rc<RefCell<TreeNode>>>=Some(Rc::new(RefCell::new(TreeNode{val:21, left:None, right:None})));
    let root: Option<Rc<RefCell<TreeNode>>>=Some(Rc::new(RefCell::new(TreeNode{val:21, left:node, right:None})));
    println!("{:?}", complete_node(vec![root], 1));
}