========================
Mermaid Sequence diagram
========================

The goal is to display the following diagram.

.. mermaid::

    sequenceDiagram
        autonumber
        Bob->>Alice: Authentication Request
        Alice->>Bob: Authentication Response

        Bob->>Alice: dummy

        Bob->>Alice: Yet another authentication Request
        Alice->>Bob: Yet another authentication Response

        Bob->>Alice: dummy

        Bob->>Alice: Yet another authentication Request
        Alice->>Bob: Yet another authentication Response
