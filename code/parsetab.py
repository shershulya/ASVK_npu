
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'deparserCOMMA DPRS HEADER HEX INT LOAD PHV PLUSdeparser : DPRS codecode : empty\n                | load codeload : LOAD header COMMA phv COMMA INTempty :phv : PHV shiftheader : HEADER shiftshift : empty\n                 | PLUS numbernumber : INT\n                  | HEX'
    
_lr_action_items = {'LOAD':([1,4,21,],[3,3,-4,]),'HEADER':([3,],[7,]),'$end':([1,2,4,5,6,9,21,],[-5,0,-5,-1,-2,-3,-4,]),'COMMA':([7,8,10,11,14,15,16,17,18,20,],[-5,13,-7,-8,-10,-9,-11,19,-5,-6,]),'PHV':([13,],[18,]),'INT':([12,19,],[14,21,]),'PLUS':([7,18,],[12,12,]),'DPRS':([0,],[1,]),'HEX':([12,],[16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'number':([12,],[15,]),'deparser':([0,],[2,]),'phv':([13,],[17,]),'header':([3,],[8,]),'shift':([7,18,],[10,20,]),'load':([1,4,],[4,4,]),'code':([1,4,],[5,9,]),'empty':([1,4,7,18,],[6,6,11,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> deparser","S'",1,None,None,None),
  ('deparser -> DPRS code','deparser',2,'p_deparser','deparser.py',33),
  ('code -> empty','code',1,'p_code','deparser.py',37),
  ('code -> load code','code',2,'p_code','deparser.py',38),
  ('load -> LOAD header COMMA phv COMMA INT','load',6,'p_load','deparser.py',45),
  ('empty -> <empty>','empty',0,'p_empty','base.py',47),
  ('phv -> PHV shift','phv',2,'p_phv','deparser.py',49),
  ('header -> HEADER shift','header',2,'p_header','deparser.py',53),
  ('shift -> empty','shift',1,'p_shift','deparser.py',57),
  ('shift -> PLUS number','shift',2,'p_shift','deparser.py',58),
  ('number -> INT','number',1,'p_number','deparser.py',65),
  ('number -> HEX','number',1,'p_number','deparser.py',66),
]
