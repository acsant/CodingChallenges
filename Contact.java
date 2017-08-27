import java.util.*;

public class Contact {

  private static String spaces = "";

  private static class TrieNode {
    private Map<Character, TrieNode> node = new HashMap<>();
    
    public boolean find( char ch ) {
      return node.containsKey(ch);
    }

    public void insert( char ch ) {
      node.put(ch, new TrieNode() );
    }

    public TrieNode getNext( char ch ) {
      return node.get(ch);
    }

    @Override
    public String toString() {
      String nodeStr = "";
      for ( Map.Entry<Character, TrieNode> entry : node.entrySet() ) 
        nodeStr += spaces + entry.getKey() + " : " + entry.getValue().toString();
      nodeStr += "\n";
      spaces += " ";
      return nodeStr;
    }
  }

  private static class Trie {
    private TrieNode root = new TrieNode();
    
    public void add( String word ) {
      System.out.println("Adding word : " + word);
      TrieNode currNode = root;
      for ( int i = 0; i < word.length(); i++ ) {
        if ( !root.find(word.charAt(i)) ) {
          currNode.insert(word.charAt(i));
        }
        currNode = currNode.getNext(word.charAt(i));
      } 
    }

    @Override
    public String toString() {
      return root.toString();
    }

    public int find( String word ) {
      return -1;
    }

  }

  private static Trie trie = new Trie();

  public static void main (String []args ) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for ( int i = 0; i < n; i++ ) {
      String command = sc.next().trim();
      String word = sc.next().trim();
      if (command.equals("add")) {
        trie.add(word);
      } else if (command.equals("find")) {
        trie.find(word);
      } else {
        printTrie(trie);
      }
    }
  }

  public static void printTrie( Trie trie ) {
    spaces = "";
    System.out.println(trie.toString());
  }

}
