class Node {
    int data;
    Node left, right;

    public Node(int item) {
        data = item;
        left = right = null;
    }
}

class BinaryTree {
    Node root;

    BinaryTree(int data) {
        root = new Node(data);
    }

    BinaryTree() {
        root = null;
    }

    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();

        // Create the tree
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);

        // Print the tree
        System.out.println("Binary Tree:");
        tree.printTree(tree.root);
    }

    void printTree(Node node) {
        if (node == null)
            return;

        // Print the node's data
        System.out.print(node.data + " ");

        // Recursively print the left and right subtrees
        printTree(node.left);
        printTree(node.right);
    }
}