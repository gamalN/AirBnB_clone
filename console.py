#!/usr/bin/python3
"""
Entry point module for Console program
"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """The Console Program"""
    prompt = "(hbnb) "

    def do_quit(self, _):
        """Quit command to exit the program"""
        sys.exit()

    def help_quit(self):
        """Prints help for quit command"""
        print("Quit command to exit the program\n\nUsage: quit")

    def do_EOF(self, _):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        return False

    def do_create(self, line):
        """Create a new instance of data models, save it (to the JSON file)
        and print the id

        Usage: create <class name>
        """
        if not line:
            print("** class name missing **")
            return
        arg = line.split()[0]
        if arg == "BaseModel":
            new = BaseModel()
        elif arg == "User":
            new = User()
        elif arg == "State":
            new = State()
        elif arg == "City":
            new = City()
        elif arg == "Amenity":
            new = Amenity()
        elif arg == "Place":
            new = Place()
        elif arg == "Review":
            new = Review()
        else:
            print("** class doesn't exist **")
            return
        new.save()
        print(new.id)

    def help_create(self):
        """Prints help for create command"""
        print("".join(["Create a new instance of data models, save it ",
                       "(to the JSON file) and print the id", "\n\n", "Usage:",
                       " create <class name>", "\n\n", "data models are: ",
                       "BaseModel, User, State, City, Amenity, Place, Review"])
              )

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in ["BaseModel", "User", "State", "City",
                           "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                key = "{}.{}".format(args[0], args[1])
                print(storage.all()[key])
            except KeyError:
                print("** no instance found **")

    def help_show(self):
        """Prints help for show command"""
        print("".join(["Prints the string representation of an instance ",
                       "based on the class name and id", "\n\n", "Usage: ",
                       "show <class name> <id>", "\n\n", "data models are: ",
                       "BaseModel, User, State, City, Amenity, Place, Review"])
              )

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in ["BaseModel", "User", "State", "City",
                           "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                key = "{}.{}".format(args[0], args[1])
                del storage.all()[key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def help_destroy(self):
        """Prints help for destroy command"""
        print("".join(["Deletes an instance based on the class name and id",
                       "\n\n", "Usage: destroy <class name> <id>", "\n\n",
                       "data models are: BaseModel, User, State, City,",
                       " Amenity, Place, Review"]))

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
        the class name"""
        args = line.split()
        if line and args[0] not in ["BaseModel", "User", "State", "City",
                                    "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        else:
            print([str(v) for v in storage.all().values()])

    def help_all(self):
        """Prints help for all command"""
        print("".join(["Prints all string representation of all instances ",
                       "based or not on the class name", "\n\n", "Usage: ",
                       "all <class name> or all", "\n\n", "data models are: ",
                       "BaseModel, User, State, City, Amenity, Place, Review"])
              )

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in ["BaseModel", "User", "State", "City",
                           "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all()[key]
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(obj, args[2], args[3])
                    storage.save()
            except KeyError:
                print("** no instance found **")

    def help_update(self):
        """Prints help for update command"""
        print("".join(["Updates data model based on the class name and id",
                       " by adding or updating attribute",  "\n\n", "Usage: ",
                       "update <class name> <id> <attribute name> ", "\n\n",
                       "data models are: BaseModel, User,",
                       " State, City, Amenity, Place, Review"]))

    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        else:
            count = 0
            for k in storage.all():
                if args[0] in k:
                    count += 1
            print(count)

    def help_count(self):
        """Prints help for count command"""
        print("".join(["Retrieves the number of instances of a class",
                       "\n\n", "Usage: count <class name>", "\n\n",
                       "data models are: BaseModel, User, State, City,",
                       " Amenity, Place, Review"]))

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        args = line.split(".")
        if len(args) == 2:
            for arg in args[1].split(","):
                arg = arg.strip()
                if arg[0] == arg[-1] == '"':
                    arg = arg[1:-1]
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.do_count(args[0])
            elif args[1][:5] == "show(" and args[1][-1] == ")":
                args[1] = args[1][5:-1]
                self.do_show(" ".join([args[0], args[1].strip('"')]))
            elif args[1][:8] == "destroy(" and args[1][-1] == ")":
                args[1] = args[1][8:-1]
                self.do_destroy(" ".join([args[0], args[1].strip('"')]))
            elif args[1][:7] == "update(" and args[1][-1] == ")":
                args[1] = args[1][7:-1]
                if "," in args[1]:
                    # FIXME: find bug with multiple key-values
                    # check and parse dictionary arguments
                    if "{" in args[1] and "}" in args[1]:
                        # extract dictionary from args[1]
                        args[1] = args[1].split(", {")
                        args[1][1] = args[1][1].split("}")[0]
                        # parse dictionary
                        args[1][1] = args[1][1].split(", ")
                        for i in range(len(args[1][1])):
                            args[1][1][i] = args[1][1][i].split(": ")
                            args[1][1][i][0] = args[1][1][i][0].strip('"')
                            args[1][1][i][1] = args[1][1][i][1].strip('"')
                        # update object
                        self.do_update(" ".join([args[0],
                                                args[1][0].strip('"')] +
                                                [f'{name} {value}'
                                                for name, value in args[1][1]])
                                       )
                    else:
                        args[1] = args[1].split(", ")
                        self.do_update(" ".join([args[0],
                                                 args[1][0].strip('"'),
                                                 args[1][1].strip('"'),
                                                 args[1][2].strip('"')]))
                else:
                    self.do_update(" ".join([args[0], args[1].strip('"')]))
        else:
            cmd.Cmd.default(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
