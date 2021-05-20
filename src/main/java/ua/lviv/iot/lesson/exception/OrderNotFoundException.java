package ua.lviv.iot.lesson.exception;

@SuppressWarnings("serial")
public class OrderNotFoundException extends Exception {

    public OrderNotFoundException(String message) {
        super(message);
    }
}
