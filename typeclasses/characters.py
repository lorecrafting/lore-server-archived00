"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    def at_post_puppet(self, **kwargs):
        """
        Called just after puppeting has been completed and all
        Account<->Object links have been established.
        Args:
            **kwargs (dict): Arbitrary, optional arguments for users
                overriding the call (unused by default).
        Note:
            You can use `self.account` and `self.sessions.get()` to get
            account and sessions at this point;the last entry in the
            list from `self.sessions.get()` is the latest Session
            puppeting this Object.
        """
        self.msg("\nYou become |c%s|n.\n" % self.name)
        # self.msg(self.at_look(self.location))
        self.show_location()

        def message(obj, from_obj):
            obj.msg("%s has entered the game." % self.get_display_name(obj), from_obj=from_obj)
        self.location.for_contents(message, exclude=[self], from_obj=self)

    def at_after_move(self, source_location):
        """
        We make sure to look around after a move.
        """
        print("characters.py at_after_move executed")
        self.msg( ("",{"msg": ("Moving to %s ...") % self.location.name}))
        self.show_location()

    def show_location(self):
        print("characters.py show_location executed")
        if self.location:
            location = self.location

            location_dbref = location.id
            location_name = location.name
            location_desc = location.db.desc
            location_contents = list(set(location.contents) - set(location.exits) - set([self]))
            location_exits = location.exits
            
            data = {
                "dbref": location_dbref,
                "name": location_name,
                "desc": location_desc,
                "contents": location_contents,
                "exits": location_exits
            }
            self.msg(("", {"current_location": data}))

    pass
