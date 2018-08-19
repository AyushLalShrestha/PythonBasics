package com.als.main;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Main {

    public static void main(String[] args) {

        int port = 5000;
        try {
            // Start a new server in a port
            ServerSocket server = new ServerSocket(port);

            //Global object stores persistent data // ClientHandler handler = new ClientHandler();

            System.out.println("Connection established at : " + port + " listening for incoming requests... . . ");
            while (true) {
                Socket client = server.accept();
                System.out.println("Connection request from pc : " + client.getInetAddress());
                // ClientListener listener = new ClientListener(client, handler);
                // listener.start();

            }
        } catch (IOException e) {
        	System.out.println(e.getMessage());
        }

    }

}
