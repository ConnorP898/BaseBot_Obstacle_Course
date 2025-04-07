myVariable = 0

def when_started1():
    global myVariable
    drivetrain.drive_for(FORWARD, 300, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 100, MM)
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 45, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 600, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 45, DEGREES)
    drivetrain.drive_for(FORWARD, 150, MM)
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    drivetrain.drive_for(FORWARD, 900, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(RIGHT, 80, DEGREES)
    drivetrain.drive_for(FORWARD, 900, MM)

when_started1()
