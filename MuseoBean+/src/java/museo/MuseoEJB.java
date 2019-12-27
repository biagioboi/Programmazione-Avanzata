/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package museo;

import java.util.List;
import javax.ejb.LocalBean;
import javax.ejb.Stateless;
import javax.inject.Inject;
import javax.interceptor.Interceptors;
import javax.persistence.EntityManager;
import javax.persistence.TypedQuery;

/**
 *
 * @author corsopd
 */
@Stateless
@LocalBean
public class MuseoEJB implements MuseoEJBRemote {
    @Inject
    EntityManager em;
    
    @Override
    public Museo createMuseo(Museo m) {
        em.persist(m);
        return m;
    }

    @Override
    public Museo updateMuseo(Museo m) {
        return em.merge(m);
    }

    @Override
    public void deleteMuseo(Museo m) {
        em.remove(em.merge(m));
    }
    
    @Interceptors(InterceptChange.class)
    public List<Museo> printByRegion(String regione) {
        TypedQuery query = em.createNamedQuery(Museo.retrieveByRegione, Museo.class);
        query.setParameter("regione", regione);
        return query.getResultList();
    }
    
    public Museo retrieveById(long id) {
        TypedQuery query = em.createNamedQuery(Museo.retrieveById, Museo.class);
        query.setParameter("id", id);
        return (Museo) query.getSingleResult();
    }

}
