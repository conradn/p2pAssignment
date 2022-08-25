public class Peer{
    
    public int id;

    public FingerTable fingertb;

    public Peer(){
        this.id = 0;
        this.fingertb = new FingerTable();
        for(int i = 0; i<3; i++){
          this.fingertb.x[i] = this.entry(id, i);
        }
    }   

    public int entry(int id, int i){
        return (int) (id + (int) Math.pow(2, i));
    }

    public void update(){
        //
    }

    public void allow_join(){
        //
    }

    public void join(){
        // join the peer to peer network
    }

    public void transfer(){
        //
    }

    public void search(){
        //
    }

    public static void main(String[] args){
        new Peer();
    }
}