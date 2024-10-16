.parser
    store PHV, HEADER, 42
    mov r1, PHV, 6
    cmpjn r1, 0xffffffffffff, halt
    mov r1, PHV+6, 6
    cmpje r1, 0xffffffffffff, halt
    
    mov r2, PHV+12, 2
    cmpjn r2, 0x0806, halt
    mov r2, 0x0000, 2
    mov r2, PHV+15, 1
    cmpjn r2, 0x1, halt
    mov r2, PHV+16, 2
    cmpjn r2, 0x0800, halt

    
.match_action 1
    mov r3, PHV+21, 1
    cmpje r3, 0x1, request
    cmpje r3, 0x2, response
request:
    mov r1, PHV+38, 4
    call exact_match
    cmpje r2, 1, not_found
    mov PHV+32, r1, 6
    mov PHV+21, 0x2, 1
    j done
response:
    mov r1, PHV+22, 6
    call exact_match
    cmpje r2, 1, not_found
    j halt
done:
not_found:
    or PORTMASK, 0xff


.deparser
    load HEADER, PHV, 42
