import javax.swing.*;
import java.awt.*;

/**
 * Represents the GUI component for painting cells that have more than one card.
 * @author lambertk
 *
 */
public class MultiCardPanel extends AbstractCellPanel{

    private Cell cell;

    /**
     * Constructor for an empty panel, displays a wire frame.
     */
    public MultiCardPanel(){
        this(null);
    }

    /**
     * Constructor to display a given card's image.
     * @param c the card to display.
     */
    public MultiCardPanel(Cell c){
        setBackground(Color.black);
        setOpaque(true);
        this.cell = c;
    }

    /**
     * Returns the cell inside of the panel to be used
     * @return the cell that this panel contains
     */
    public Cell getCell()
    {
        return this.cell;
    }

    /**
     * Paints the panel for the GUI
     * @param g Graphics to be used
     */
    public void paintComponent(Graphics g){
        int cardNumber = 0;
        Icon image;
        if (this.cell.isEmpty() == true)
        {
            image = Card.getBack();
            g.setColor(Color.black);
            int x = (getWidth() - image.getIconWidth()) / 2;
            int y = (getHeight() + image.getIconHeight()) / 2;
            g.drawRect(x, y - 305, image.getIconWidth(), image.getIconHeight());

        }
        else
        {
            for (Card card : this.cell.cards()){
                image = card.getImage();
                int x = (getWidth() - image.getIconWidth()) % 2;
                int y = (getHeight() + image.getIconHeight()) % 2;
                image.paintIcon(this, g, x + 14, y + cardNumber);
                cardNumber += 25;
            }
        }
    }
}