package rmi.cliente;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.util.Scanner;

import rmi.server.ServerInterface;

public class ClienteMain {

	private static Scanner scanner;

	public static void main(String[] args) throws MalformedURLException, RemoteException, NotBoundException {
		scanner = new Scanner(System.in);
		String name = null;
		String URIserver = "rmi://localhost/ChatServer";
		ServerInterface server = (ServerInterface) Naming.lookup(URIserver);

		// Recebe o nome (identificador) do cliente
		System.out.println("Digite seu nick: ");
		try {
			name = scanner.nextLine();
		} catch (Exception e) {
			e.printStackTrace();
		}
		// Inicia as operações do cliente.
		new Thread(new Cliente(name, server)).start();
	}
}
