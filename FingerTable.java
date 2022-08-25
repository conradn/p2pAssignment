import java.io.Serializable;

public class FingerTable implements Serializable {
    int x[] = new int[3];
    int i[] = new int[3];
    int s[] = new int[3];

    public FingerTable(){
        this.i[0] = 0;
        this.i[1] = 1;
        this.i[2] = 2;
    }
}
