package rmi.server;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.RemoteException;

public class ServerMain {
	public static void main(String[] args) throws RemoteException, MalformedURLException {
		try {
			// Inicia o servidor
			Naming.rebind("ChatServer", new Server());
		} catch (Exception e) {
			System.out.println("Err: " + e.getMessage());
      e.printStackTrace();
		}
	}
}
