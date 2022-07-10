import javax.swing.*;

/**
 * Represents a playing card with a suit,
 * rank, image, and face up status.
 * @author lambertk
 */
public class Card implements Comparable<Card>{

    private Suit suit;
    private int rank;
    private int color;
    private boolean faceUp;
    private Icon image;
    private static Icon CARD_BACK;

    /**
     * Constructor.
     * @param suit the card's suit
     * @param rank the card's rank
     */
    public Card(Suit suit, int rank){
        this.suit = suit;
    	this.rank = rank;
      if(this.suit == Suit.spade || this.suit == Suit.club){
        this.color = 0;
      }
      if(this.suit == Suit.heart || this.suit == Suit.diamond){
        this.color = 1;
      }

    	faceUp = true;
    	image = getImageFromFile(rank, suit);
    	if (CARD_BACK == null)
    		CARD_BACK = getBackFromFile();
    }

    /**
     * Returns the card's face image if its face is up or its back side image otherwise.
     * @return the card's face image or the back side image
     */
    public Icon getImage(){
    	if (faceUp)
    	    return image;
    	else
    	    return CARD_BACK;
    }

    /**
     * Returns the back side image of a card.
     * @return the back side image of a card
     */
    public static Icon getBack(){
    	if (CARD_BACK == null)
    	    new Card(Suit.spade, 1);
    	return CARD_BACK;
    }

    /**
     * Turns the card over, negating its face up status.
     */
    public void turn(){
    	faceUp = ! faceUp;
    }

    private Icon getImageFromFile(int rank, Suit suit){
    	String fileName = "DECK/";
    	fileName += rank;
    	fileName += Character.toUpperCase(suit.toString().charAt(0));
    	fileName += ".GIF";
    	return new ImageIcon(getClass().getResource(fileName));
    }

    private Icon getBackFromFile(){
    	String fileName = "DECK/CARDBACK.GIF";
    	return new ImageIcon(getClass().getResource(fileName));
    }

    /**
     * Returns the card's face up status.
     * @return true if face up or false otherwise
     */
    public boolean isFaceUp(){
       return faceUp;
    }

    /**
     * Returns the card's suit.
     * @return the card's suit
     */
    public Suit getSuit(){
        return suit;
    }

    /**
     * Returns the card's rank
     * @return the card's rank
     */
    public int getRank(){
        return rank;
    }

    /**
     * Gives the color of the card
     * @return the color of the card
     */
    public int getColor(){
      return color;
    }

    /**
     * Compares two cards with respect to rank
     * @return 0 if equal, less than 0 if less, greater than 0 if greater
     */
    public int compareTo(Card other){
        return this.rank - other.rank;
    }

    /**
     * Returns the string representation of the card (rank of suit)
     * @return the string representation of the card
     */
    public String toString(){
        return rankToString(rank) + " of " + suit;
    }

    /**
     * String representation of card
     * @param rank the rank of the card
     * @return string representation of the card
     */
    static private String rankToString(int rank){
        if (rank >= 2 && rank <= 10) return rank + "";
        else if (rank == 11) return "Jack";
        else if (rank == 12) return "Queen";
        else if (rank == 13) return "King";
        else return "Ace";
    }
}
