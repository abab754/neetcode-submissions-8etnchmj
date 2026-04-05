static class Singleton {
    private static Singleton instance;
    private String val;

    private Singleton() {
    }

    public static Singleton getInstance() {
        if(instance == null){
            instance = new Singleton();
        }
        return instance;
    }

    public String getValue() {
        return this.val;
    }

    public void setValue(String value) {
        this.val = value;
    }
    
}
