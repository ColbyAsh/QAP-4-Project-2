public class Main {
    // MotelCustomer object definition
    function MotelCustomer(name, birthDate, gender, roomPreferences, paymentMethod, mailingAddress, phoneNumber, checkInDate, checkOutDate) {
        this.name = name;
        this.birthDate = birthDate;
        this.gender = gender;
        this.roomPreferences = roomPreferences;
        this.paymentMethod = paymentMethod;
        this.mailingAddress = mailingAddress;
        this.phoneNumber = phoneNumber;
        this.checkInDate = checkInDate;
        this.checkOutDate = checkOutDate;
    
        // Method to calculate age
        this.calculateAge = function() {
            const currentDate = new Date();
            const birthYear = new Date(this.birthDate).getFullYear();
            return currentDate.getFullYear() - birthYear;
        };
    
        // Method to calculate duration of stay
        this.calculateStayDuration = function() {
            const checkIn = new Date(this.checkInDate);
            const checkOut = new Date(this.checkOutDate);
            const millisecondsPerDay = 24 * 60 * 60 * 1000;
            return Math.round(Math.abs((checkOut - checkIn) / millisecondsPerDay));
        };
    
        // Method to generate a description of the customer
        this.generateCustomerDescription = function() {
            const age = this.calculateAge();
            const durationOfStay = this.calculateStayDuration();
    
            // Template literal string describing the customer
            const description = `
                ${this.name} is a ${age}-year-old ${this.gender} who has booked a room at our motel. 
                They prefer ${this.roomPreferences.join(', ')} and will be staying with us for ${durationOfStay} days. 
                They will be checking in on ${this.checkInDate} and checking out on ${this.checkOutDate}. 
                For payment, they will be using ${this.paymentMethod}.
                Contact them at ${this.phoneNumber} or reach out to their mailing address at ${mailingAddress.street}, 
                ${mailingAddress.city}, ${mailingAddress.state} ${mailingAddress.zip}.
            `;
    
            return description;
        };
    }
    
    // Example usage
    const customer = new MotelCustomer(
        'John Doe',
        '1990-05-15',
        'Male',
        ['Non-smoking', 'Double bed'],
        'Credit Card',
        {
            street: '123 Main St',
            city: 'Cityville',
            state: 'CA',
            zip: '12345'
        },
        '555-1234',
        '2023-01-15',
        '2023-01-20'
    );
    
    // Display customer description
    console.log(customer.generateCustomerDescription());

    
}
