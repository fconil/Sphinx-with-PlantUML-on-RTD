=========================
PlantUML Sequence diagram
=========================

The goal is to display the following diagram.

.. uml::

    !theme aws-orange

    autonumber 10 10 "<b>[000]"

    Bob -> Alice : Authentication Request
    Bob <- Alice : Authentication Response

    autonumber stop
    Bob -> Alice : dummy

    autonumber resume "<font color=red><b>Message 0  "
    Bob -> Alice : Yet another authentication Request
    Bob <- Alice : Yet another authentication Response

    autonumber stop
    Bob -> Alice : dummy

    autonumber resume 1 "<font color=blue><b>Message 0  "
    Bob -> Alice : Yet another authentication Request
    Bob <- Alice : Yet another authentication Response

