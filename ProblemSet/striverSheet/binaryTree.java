class Node{
    int data;
    Node left;
    Node right;
    public Node(int data){
        this.data = data;
        this.left = null;
        this.right = null;
    }   
}
class Binary{
    public Node BinaryTree(){
        Node root = new Node(1);
        root.left = new Node(2);    
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        return root;
    }
}
public class binaryTree{
    public static void main(String[] args) {
        Binary b = new Binary();
        Node root = b.BinaryTree();
        System.out.println(root.data);
        System.out.println("Left: "+root.left.data);
        System.out.println("Right: "+root.right.data);
        System.out.println(root.left.data +" Left "+root.left.left.data);
        System.out.println(root.left.data +" Right "+root.left.right.data);
    }
}