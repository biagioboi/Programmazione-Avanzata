/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package museo;

import java.io.Serializable;

/**
 *
 * @author corsopd
 */
// ho dimenticato di mettere implements Serializable
public class MessageDTO implements Serializable {
    private long idMuseo;
    private int numVisitatori;

    public MessageDTO(long idMuseo, int numVisitatori) {
        this.idMuseo = idMuseo;
        this.numVisitatori = numVisitatori;
    }

    public long getIdMuseo() {
        return idMuseo;
    }

    public void setIdMuseo(long idMuseo) {
        this.idMuseo = idMuseo;
    }

    public int getNumVisitatori() {
        return numVisitatori;
    }

    public void setNumVisitatori(int numVisitatori) {
        this.numVisitatori = numVisitatori;
    }
    
    
}
