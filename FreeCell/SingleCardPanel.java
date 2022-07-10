import javax.swing.*;
import java.awt.*;

/**
 * Panel to be used for cells that have one card
 * @author lambertk
 */
public class SingleCardPanel extends AbstractCellPanel{

    private Cell cell;
    private Color frameColor = Color.yellow;

    /**
     * Constructor for an empty panel, displays a wire frame.
     */
    public SingleCardPanel(){
        this(null);
    }

    /**
     * Constructor to display a given card's image.
     * @param c the card to display.
     */
    public SingleCardPanel(Cell c){
        setBackground(Color.green);
        this.cell = c;
    }

    /**
     * Returns the cell the panel represents to be used
     * @return the cell that the panel contains
     */
    public Cell getCell()
    {
        return this.cell;
    }

    /**
     * Sets the frame color of the panel
     * @param isHome checks to see if the panel is a home cell
     */
    public void setFrameColor(boolean isHome){
      if (isHome){
        frameColor = Color.white;
      }
      else{
        frameColor = Color.yellow;
      }
    }

    /**
     * Paints the panel for the GUI
     * @param g graphics to be use
     */
    public void paintComponent(Graphics g){
        int cardNumber = 0;

        Icon image;
        if (this.cell.isEmpty() == true){
            image = Card.getBack();
            g.setColor(frameColor);
            int x = (getWidth() - image.getIconWidth()) / 2;
            int y = (getHeight() - image.getIconHeight()) / 2;
            g.drawRect(x, y, image.getIconWidth(), image.getIconHeight());
        }
        else{
            Card card = cell.peekTop();
            image = card.getImage();
            int x = (getWidth() - image.getIconWidth()) / 2;
            int y = (getHeight() - image.getIconHeight()) / 2;
            image.paintIcon(this, g, x, y);
        }
    }
}
