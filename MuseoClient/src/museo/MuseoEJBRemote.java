/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package museo;

import java.util.List;
import javax.ejb.Remote;

/**
 *
 * @author corsopd
 */
@Remote
public interface MuseoEJBRemote {
    public Museo createMuseo(Museo m);
    public Museo updateMuseo(Museo m);
    public void deleteMuseo(Museo m);
    public List<Museo> printByRegion(String regione);
    public Museo retrieveById(long id);
}
