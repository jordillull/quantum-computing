
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\r\x1e\xd33\xb6\xeb+\x83\xcf\x99\x1dl\xff\xd0\x8c>'
    
_lr_action_items = {'$end':([2,3,4,],[0,-1,-2,]),'BITSTRING':([3,],[4,]),'INITIALIZE':([0,],[1,]),'REGISTER':([1,],[3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'op_initialize':([0,],[2,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> op_initialize","S'",1,None,None,None),
  ('op_initialize -> INITIALIZE REGISTER','op_initialize',2,'p_initialize','./qshell.py',12),
  ('op_initialize -> INITIALIZE REGISTER BITSTRING','op_initialize',3,'p_initialize','./qshell.py',13),
  ('op_select -> SELECT VARIABLE REGISTER DIGIT DIGIT','op_select',5,'p_select','./qshell.py',17),
  ('op_apply -> APPLY matrix REGISTER','op_apply',3,'p_apply','./qshell.py',21),
  ('matrix -> gate','matrix',1,'p_matrix','./qshell.py',37),
  ('matrix -> VARIABLE','matrix',1,'p_matrix','./qshell.py',38),
  ('gate -> CNOT','gate',1,'p_gate','./qshell.py',42),
  ('gate -> H','gate',1,'p_gate','./qshell.py',43),
  ('gate -> identity','gate',1,'p_gate','./qshell.py',44),
  ('identity -> IMATRIX','identity',1,'p_identity','./qshell.py',48),
  ('whatever -> CNOT','whatever',1,'p_whatever','./qshell.py',52),
]
