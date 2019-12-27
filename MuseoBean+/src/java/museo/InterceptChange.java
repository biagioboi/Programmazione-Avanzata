/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package museo;

import javax.interceptor.AroundInvoke;
import javax.interceptor.Interceptor;
import javax.interceptor.InvocationContext;

/**
 *
 * @author corsopd
 */
@Interceptor
public class InterceptChange {
    private int cont;
    
    //ho dimenticato di mettere il  throws Exception, o la gestione dell'eccezione
    @AroundInvoke
    public Object contatore(InvocationContext ic) throws Exception {
        cont++;
        System.out.println("Il metodo e' stato invocato " + cont + " volte");
        return ic.proceed();
    }
}
