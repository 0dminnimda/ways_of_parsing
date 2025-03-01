# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : parser.sm

import statemap


class ParserState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def next(self, fsm):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)

class StateMap_Default(ParserState):

    def next(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(StateMap.unexpected)
        fsm.getState().Entry(fsm)


class StateMap_unexpected(StateMap_Default):
    pass

class StateMap_start(StateMap_Default):

    def next(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.peek().isdigit()  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.start_number()
                ctxt.consume()
            finally:
                fsm.setState(StateMap.number)
                fsm.getState().Entry(fsm)
        else:
            StateMap_Default.next(self, fsm)
        
class StateMap_number(StateMap_Default):

    def next(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.peek().isdigit()  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.consume()
            finally:
                fsm.setState(StateMap.number)
                fsm.getState().Entry(fsm)
        elif  ctxt.peek() == "+"  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.end_number()
                ctxt.save_op()
                ctxt.consume()
            finally:
                fsm.setState(StateMap.operator)
                fsm.getState().Entry(fsm)
        elif  ctxt.peek() == "-"  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.end_number()
                ctxt.save_op()
                ctxt.consume()
            finally:
                fsm.setState(StateMap.operator)
                fsm.getState().Entry(fsm)
        elif  ctxt.peek() == ""  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.end_number()
            finally:
                fsm.setState(StateMap.end)
                fsm.getState().Entry(fsm)
        else:
            StateMap_Default.next(self, fsm)
        
class StateMap_operator(StateMap_Default):

    def next(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.peek().isdigit()  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.start_number()
                ctxt.consume()
            finally:
                fsm.setState(StateMap.number_2)
                fsm.getState().Entry(fsm)
        else:
            StateMap_Default.next(self, fsm)
        
class StateMap_number_2(StateMap_Default):

    def next(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.peek().isdigit()  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.consume()
            finally:
                fsm.setState(StateMap.number_2)
                fsm.getState().Entry(fsm)
        else:
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(StateMap.number)
            fsm.getState().Entry(fsm)


class StateMap_end(StateMap_Default):
    pass

class StateMap(object):

    unexpected = StateMap_unexpected('StateMap.unexpected', 0)
    start = StateMap_start('StateMap.start', 1)
    number = StateMap_number('StateMap.number', 2)
    operator = StateMap_operator('StateMap.operator', 3)
    number_2 = StateMap_number_2('StateMap.number_2', 4)
    end = StateMap_end('StateMap.end', 5)
    Default = StateMap_Default('StateMap.Default', -1)

class Parser_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, StateMap.start)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:
