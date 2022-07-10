/**
 * A <code>AbstractCell</code> abstract cell class to give shared methods to other cells
 * @author Bryce Burnette
 * @author Ana Estrada Hamm
 * @author Evan Phaup
 * file: AbstractCell.java
 */

import java.util.*;

/**
 * Abstract cell class to be used in cell implementation
 * Implements Cell interface
 */
abstract public class AbstractCell implements Cell{

  protected ArrayList<Card> cards = new ArrayList <Card>();
  protected int MAX_SIZE;

  /**
   * initializes an abstract sell
   * @param max max size of the cell
   */
  public AbstractCell(int max){
    cards = new ArrayList <Card>();
    MAX_SIZE = max;
  }

  /**
   * Adds a card to a cell without rules
   * Used for dealing, group adding, and testing purposes
   * @param c The card to add to the pile
   */
  public void add(Card c){
    this.cards.add(c);
  }

  /**
   * Returns true or false based on whether you can use a top card or not
   * @return boolean that is true if the card can move
   */
  public boolean canMoveFrom(Cell from){
    if (cards.size() == this.maxSize() || from.isEmpty() || from instanceof HomeCell){
      return false;
    }
    return true;

  /**
   * Tells whether or not the cell is empty
   * @return true if the cell is empty
   */
  }
  public boolean isEmpty(){
    if (cards.size() == 0){
      return true;
    }
    return false;
  }

  /**
   * Gives the card at the top of the cell
   * @return card on top of the cell?
   */
  public Card peekTop(){
    if (this.isEmpty() == false)
    {
      return cards.get(cards.size() - 1);
    }
    return null;
  }

  /**
   * Removes and returns the card at the top of the cell
   * @return Card at the top of the cell
   */
  public Card getTop(){
    Card card = cards.get(cards.size() - 1);
    cards.remove(cards.size() - 1);
    return card;
  }

  /**
   * Adds the top card from another cell
   * @param from Cell to add card from
   */
  public void addFrom(Cell from){
    if (canMoveFrom(from))
    {
      cards.add(from.getTop());
    }
  }

  /**
   * Gives the size of the cell
   * @return int that is the size of the cell
   */
  public int size(){
    return cards.size();
  }

  /**
   * Clears the cell
   */
  public void clear(){
    cards.clear();
  }

  /**
   * Allows the cards to be used, helpful for moving groups
   * @return The cards in a cell to be used
   */
  public ArrayList<Card> cards(){
    return cards;
  }

  /**
   * Gives the max size for the cell
   * @return int that represents the max size of the cell
   */
  public int maxSize(){
    return MAX_SIZE;
  }
  public Iterator<Card> iterator(){
    return cards.iterator();
  }

  /**
   * Gives a string representation of the cell
   * @return String representation of the cell
   */
  public String toString(){
    String str = "";
    for (Card card : cards)
    {
      str += card.toString() + " ";
    }
    return str;
  }
}
